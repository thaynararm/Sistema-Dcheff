const urlUf = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados'
const city = document.getElementById("city")
const uf = document.getElementById("uf")

uf.addEventListener('change', async function(){
    let urlCities;
    if(uf.value == 'DF'){
        urlCities = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados/'+uf.value+'/subdistritos';
    } else {
        urlCities = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados/'+uf.value+'/municipios';
    }
    const request = await fetch(urlCities);
    const response = await request.json();

    response.sort((a, b) => a.nome.localeCompare(b.nome))

    let options = ''

    response.forEach(function(city){
        options += '<option>' + city.nome + '</option>'
    })
    city.innerHTML = options
})


window.addEventListener('load', async ()=>{
    const request = await fetch(urlUf);
    const response = await request.json();

    response.sort((a, b) => a.nome.localeCompare(b.nome));

    const options = document.createElement('optgroup');

    options.innerHTML += '<option disabled selected value>Selecione o Estado</option>';

    response.forEach(function(uf){
        options.innerHTML += '<option>' + uf.sigla + '</option>'
    })

    uf.append(options)
})