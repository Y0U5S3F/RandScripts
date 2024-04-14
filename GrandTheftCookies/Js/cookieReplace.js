const axios = require('axios');

// Replace these values with your actual cookies
const cookies = {
    'c_user': '100049715811507',
    'datr': '__GMZCgwVF5BbyvAtfJojQwg',
    'fr': '0MXYL1rsdRNMYwFR5.AWVs3oG-QIPY6dDanXEIvG9G6jc.Bl0IQ8..AAA.0.0.BmEqt3.AWUqazr9gIo',
    'oo': 'v1',
    'presence': 'C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1712499708234%2C%22v%22%3A1%7D',
    'ps_l': '0',
    'ps_n': '0',
    'sb': 'LITQZYHpGDS-JDeYWRrr9wB5',
    'wd': '556x967',
    'xs': '14%3AfHEFD5KRL0x0Zg%3A2%3A1708164157%3A-1%3A12169%3A%3AAcVnFPp_VUYma3toB8ghBobyfyJEPAAQ7LR5RzFuGBY'
};

// Convert the cookies object into a string
const cookieString = Object.entries(cookies).map(([key, value]) => `${key}=${value}`).join('; ');

axios.get('https://www.facebook.com', {
    headers: {
        'Cookie': cookieString
    }
})
.then(response => {
    console.log(response.data);
})
.catch(error => {
    console.error(error);
});
