//PokeAPI

var pokiImg = document.querySelector('.poki_img')

var pokiForm = document.querySelector('#poki_finder')

pokiForm.addEventListener('submit', function (event) {
    event.preventDefault()

    let poki = pokiForm.children[0].value

    fetch(`https://pokeapi.co/api/v2/pokemon/${poki}`)
        .then(response => response.json())
        .then(data => {
            let img = data.sprites.front_default;
            let name = data.name

            pokiImg.innerHTML += `
        <img src="${img}" alt="Pokemon Img">
        <p>${name}</P>
        `
        })
        .catch(err => console.log(err))
})


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