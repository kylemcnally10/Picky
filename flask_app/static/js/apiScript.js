//Yelp API

let queryURL = "https://api.yelp.com/v3/businesses/search";
let apiKey = "CXHzHSza09AFAe5RV5N0y_e-O8a0k4tFdFqGznQYtnvnhtu07PxKjaRl0zx3kkXvraPc1S86SsX6Lk_NgbUoJBf0WI2b-_LHdtq3Zn-riRNEUQQ-5i5ofolRUgIAY3Yx"

$.ajax({
    url: queryURL,
    method: "GET",
    dataType: 'jsonp',
    headers: {
        "accept": "application/json",
        "x-requested-with": "xmlhttprequest",
        "Access-Control-Allow-Origin": "*",
        "Authorization": `Bearer ${apiKey}`
    }
})

// $.ajax({
//     url: 'https://api.yelp.com/v3/businesses/search?limit=50"',
//     dataType: 'jsonp',
//     data: { term: 'restaurant', location: 'irvine' }, // callback is not necessary
//     success: function (data) {
//         // data is a normal response shown on yelp's API page
//     }
// });