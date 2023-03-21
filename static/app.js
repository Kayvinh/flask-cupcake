const CUPCAKELIST = document.querySelector('#cupcake-list');
const $cupcakeList = $('#cupcake-list')



async function fetchCupcakes() {
    const response = await axios.get(`/api/cupcakes`);

    return response.data;
}

async function displayCupcakeList() {
    const data = await fetchCupcakes();

    const cupcakeObj = data.cupcakes[0];
    console.log(cupcakeObj);
    
    const $div = $("<div>");
    for (let item in cupcakeObj) {
        $div.append(cupcakeObj[item])
    }

    $cupcakeList.append($div);
}

