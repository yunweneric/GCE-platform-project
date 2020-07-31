// Loading Dependencies
const fs = require('fs');
const pdf = require('pdf-parse');

// Loading pdf
// let dataBuffer = fs.readFileSync('pdfs/2019-algen.pdf');
let dataBuffer = fs.readFileSync('pdfs/2019-olgen.pdf');
// let dataBuffer = fs.readFileSync('pdfs/2019-altech.pdf');
// let dataBuffer = fs.readFileSync('pdfs/2019-oltech.pdf');

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

    // Storing extracted content
    var content = data.text;

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
    Data = Data.replace(/Sanctioned : \d+/g, "\n");
    Data = Data.replace(/Centre No:  /g, '\n\n\n\n"Centre No": ');
    Data = Data.replace(/Regist:/g, '\nRegist:');
    Data = Data.replace(/Sat for 2 or more Subjects:/g, '\nSat for 2 or more Subjects: ');
    Data = Data.replace(/Results of Successful Candidates In Order Of Merit/g, "");
    Data = Data.replace(/% Passed : /g, '\n%Passed: ');
    Data = Data.replace(/ Passed : /g, '\nPassed: ');
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

    console.log(Data);

});
