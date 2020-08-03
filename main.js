// Loading Dependencies
const fs = require('fs');
const pdf = require('pdf-parse');
const express = require('express');

const app = express();

// const router = app.router();

// app.use('/',(req,res,next) => {
//     res.send('HEllo WOrld')
// }); 

// app.listen(4000);

// Loading pdf
// let dataBuffer = fs.readFileSync('pdfs/2019-algen.pdf');
let dataBuffer = fs.readFileSync('pdfs/2019-olgen.pdf');
// let dataBuffer = fs.readFileSync('pdfs/2019-altech.pdf');
// let dataBuffer = fs.readFileSync('pdfs/2019-oltech.pdf');

pdf(dataBuffer).then(function (data) {
    // Storing extracted content
    var content = data.text;

    
    // document.getElementById('content').innerHTML = content;

    // Replacing banners
    let Data = content.replace(/2019 RESULTS: GCE ADVANCED LEVEL GENERAL/g, "");
    Data = Data.replace(/2019 RESULTS: GCE ORDINARY LEVEL GENERAL/g, "");
    Data = Data.replace(/2019 RESULTS: GCE ORDINARY LEVEL TECHNICAL/g, "");
    Data = Data.replace(/2019 RESULTS: GCE ADVANCED LEVEL TECHNICAL/g, "");


    // Other modifications on data
    Data = Data.replace(/\n/g, "");

    Data = Data.replace(/\d+of\d+\w+/g, "");
    Data = Data.replace(/Passed In \d+ Subjects: \d+/g, "");
    Data = Data.replace(/Passed In \d+ Subjects:\d+/g, "");
    Data = Data.replace(/ In \d+ Subjects: \d+/g, "");
    // Data = Data.replace(/Sanctioned : \d+/g, "\n");
    // Data = Data.replace(/Centre No:  /g, '\n\n\n\n"Centre No": ');
    // Data = Data.replace(/Regist:/g, '\nRegist:');
    // Data = Data.replace(/Sat for 2 or more Subjects:/g, '\nSat for 2 or more Subjects: ');
    Data = Data.replace(/Results of Successful Candidates In Order Of Merit/g, "");
    // Data = Data.replace(/% Passed : /g, '\n%Passed: ');
    // Data = Data.replace(/ Passed : /g, '\nPassed: ');
    Data = Data.replace(/\(\d+\)/g, "");
    Data = Data.replace(/\(/g, "");




    // Technical section modifications
    Data = Data.replace(/Passed In Accounting Specialty: \d+/g, "");
    Data = Data.replace(/Passed In Accounting Specialty/g, "");
    Data = Data.replace(/Passed In Single Subjects: \d+/g, "");
    Data = Data.replace(/Passed In Single Subjects/g, "");
    Data = Data.replace(/Passed In Building Construction Specialty: \d+/g, "");
    Data = Data.replace(/Passed In Business Studies Specialty: \d+/g, "");
    Data = Data.replace(/Passed In Electrical Technology Specialty: \d+/g, "");
    Data = Data.replace(/Passed In Motor Mechanics Specialty: \d+/g, "");
    Data = Data.replace(/In Building Construction Specialty:  \d+/g, "");




    Data = Data.replace(/HIS-A/g, "HIS-A ");
    Data = Data.replace(/HIS-B/g, "HIS-B ");
    Data = Data.replace(/HIS-C/g, "HIS-C ");

    Data = Data.replace(/GEO-A/g, "GEO-A ");
    Data = Data.replace(/GEO-B/g, "GEO-B ");
    Data = Data.replace(/GEO-C/g, "GEO-C ");

    Data = Data.replace(/MAT-A/g, "MAT-A ");
    Data = Data.replace(/MAT-B/g, "MAT-B ");
    Data = Data.replace(/MAT-C/g, "MAT-C ");

    Data = Data.replace(/CHE-A/g, "CHE-A ");
    Data = Data.replace(/CHE-B/g, "CHE-B ");
    Data = Data.replace(/CHE-C/g, "CHE-C ");

    Data = Data.replace(/BIO-A/g, "BIO-A ");
    Data = Data.replace(/BIO-B/g, "BIO-B ");
    Data = Data.replace(/BIO-C/g, "BIO-C ");


    Data = Data.replace(/ECO-A/g, "ECO-A ");
    Data = Data.replace(/ECO-B/g, "ECO-B ");
    Data = Data.replace(/ECO-C/g, "ECO-C ");

    Data = Data.replace(/PHY-A/g, "PHY-A ");
    Data = Data.replace(/PHY-B/g, "PHY-B ");
    Data = Data.replace(/PHY-C/g, "PHY-C ");

    Data = Data.replace(/REL-A/g, "REL-A ");
    Data = Data.replace(/REL-B/g, "REL-B ");
    Data = Data.replace(/REL-C/g, "REL-C ");

    Data = Data.replace(/LOG-A/g, "LOG-A ");
    Data = Data.replace(/LOG-B/g, "LOG-B ");
    Data = Data.replace(/LOG-C/g, "LOG-C ");

    Data = Data.replace(/COM-A/g, "COM-A ");
    Data = Data.replace(/COM-B/g, "COM-B ");
    Data = Data.replace(/COM-C/g, "COM-C ");

    Data = Data.replace(/LIT-A/g, "LIT-A ");
    Data = Data.replace(/LIT-B/g, "LIT-B ");
    Data = Data.replace(/LIT-C/g, "LIT-C ");


    Data = Data.replace(/HBI-A/g, "HBI-A ");
    Data = Data.replace(/HBI-B/g, "HBI-B ");
    Data = Data.replace(/HBI-C/g, "HBI-C ");


    Data = Data.replace(/CZE-A/g, "CZE-A ");
    Data = Data.replace(/CZE-B/g, "CZE-B ");
    Data = Data.replace(/CZE-C/g, "CZE-C ");

    Data = Data.replace(/ENG-A/g, "ENG-A ");
    Data = Data.replace(/ENG-B/g, "ENG-B ");
    Data = Data.replace(/ENG-C/g, "ENG-C ");

    Data = Data.replace(/FRE-A/g, "FRE-A ");
    Data = Data.replace(/FRE-B/g, "FRE-B ");
    Data = Data.replace(/FRE-C/g, "FRE-C ");

    Data = Data.replace(/AMA-A/g, "AMA-A ");
    Data = Data.replace(/AMA-B/g, "AMA-B ");
    Data = Data.replace(/AMA-C/g, "AMA-C ");

    Data = Data.replace(/CSC-A/g, "CSC-A ");
    Data = Data.replace(/CSC-B/g, "CSC-B ");
    Data = Data.replace(/CSC-C/g, "CSC-C ");

    Data = Data.replace(/SBEF-A/g, "SBEF-A ");
    Data = Data.replace(/SBEF-B/g, "SBEF-B ");
    Data = Data.replace(/SBEF-C/g, "SBEF-C ");

    Data = Data.replace(/\d+/g, "");

    app.use('/',(req,res,next) => {
        // res.send(content)
        let finalData = Data.replace('\n/g','').split(':');
        finalData = finalData.join();
        finalData = finalData.split('Centre No,');
        var newData = [];
        finalData.forEach(data => {
            // data = data.append(',');
            newData.push(data.split(','));
        })
         newData.shift();
         var lastData = [];
         newData.forEach(data => {
             let dt = data.splice(8);
             lastData.push(dt);
             
         })

         var ld = [];

         lastData.forEach(data => {
            // for(let i = 0; i < data.length; i++){
            //     ld.push(data[i])
            // }
            let arr = data;
            arr[arr.length - 1] = arr[arr.length - 1] + ',';
            ld.push(...arr)
         })

        res.send(ld.join().replace(',,/g',','))
    }); 
    
    app.listen(4000);
    // console.log(Data);

});
