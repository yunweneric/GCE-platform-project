const fs = require('fs');
const pdf = require('pdf-parse');

let dataBuffer = fs.readFileSync('pdfs/2019-algen.pdf');

pdf(dataBuffer).then(function (data) {

    // number of pages
    // console.log(data.numpages);
    // number of rendered pages
    // console.log(data.numrender);
    // PDF info
    // console.log(data.info);
    // PDF metadata
    // console.log(data.metadata); 
    // PDF.js version
    // check https://mozilla.github.io/pdf.js/getting_started/
    // console.log(data.version);
    // PDF text
    // console.log(data.text);
    var content = data.text;
    let Data = content.replace(/2019 RESULTS: GCE ADVANCED LEVEL GENERAL/g, "");
    Data = Data.replace(/\n/g, "");
    Data = Data.replace(/\d+of\d+\w+/g, "");
    Data = Data.replace(/Passed In \d+ Subjects: \d+/g, "");
    Data = Data.replace(/Passed In \d+ Subjects:\d+/g, "");
    Data = Data.replace(/ In \d+ Subjects: \d+/g, "");



    Data = Data.replace(/Sanctioned : \d+"/g, "");
    Data = Data.replace(/Centre No:  /g, '\n\n\n\n"Centre No": ');
    Data = Data.replace(/Regist:/g, '\nRegist:');
    Data = Data.replace(/Sat for 2 or more Subjects:/g, '\nSat for 2 or more Subjects: ');
    Data = Data.replace(/Results of Successful Candidates In Order Of Merit/g, "");
    Data = Data.replace(/% Passed : /g, '\n%Passed: ');
    Data = Data.replace(/ Passed : /g, '\nPassed: ');
    console.log(Data);


    //

});
