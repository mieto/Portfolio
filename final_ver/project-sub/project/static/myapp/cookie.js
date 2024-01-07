var hourly_rate = document.getElementById('hourly_rate');
function writeCookie(){
    var cookieValue = hourly_rate.value;
    document.cookie = 'hourly_rate' + cookieValue;
    console.log(document.cookie); 
}

