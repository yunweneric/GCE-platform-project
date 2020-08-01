// $(window).on("load",function(){
//     $(".loader-wrapper").fadeOut("slow");
// });

function getValues(obj, key) {
    var objects = [];
    for (var i in obj) {
        if (!obj.hasOwnProperty(i)) continue;
        if (typeof obj[i] == 'object') {
            objects = objects.concat(getValues(obj[i], key));
        } else if (i == key) {
            objects.push(obj[i]);
        }
    }
    return objects;
}


let form = document.getElementById('form1');
form.addEventListener('submit', (e) => {
    e.preventDefault();

    var rawFile = new XMLHttpRequest();
    rawFile.overrideMimeType("application/json");
    rawFile.open("GET", "/dictionary.json", true);
    rawFile.onreadystatechange = function () {
        if (rawFile.readyState === 4 && rawFile.status == "200") {

            let data = JSON.parse(this.responseText),
             
                username = form.querySelector("input[type=text]").value.toLowerCase(),
                resultat = getValues(data, username);

                console.log(resultat);
                console.log(username);

            document.getElementById("result").innerHTML = resultat[0];



        }
    }
    rawFile.send(null);


    /* var res = new XMLHttpRequest();
 
 
     res.onreadystatechange = function() {
         if (this.readyState == 4 && this.status == 200) {
             document.getElementById("result").innerHTML =
             this.responseText;
             console.log(this);
         }
     };
 
     res.open("get", "/app.html", true);
     res.send();*/

});