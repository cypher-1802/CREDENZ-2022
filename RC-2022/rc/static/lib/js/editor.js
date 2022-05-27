ace.require("ace/ext/language_tools");

const executeCodeBtn = document.querySelector('.editor_run');
const resetCodeBtn = document.querySelector('.editor_reset');

let codeEditor = ace.edit("editorCode");

let editorLib = {
    init() {
        // codeEditor.setValue("#include <stdio.h>\n\n\nint main() {\n    // Complete the code.\n    return 0;\n}\n");
        codeEditor.clearSelection();

        // Theme
        codeEditor.setTheme("ace/theme/tomorrow_night");

        // set lang
        codeEditor.getSession().setMode("ace/mode/c_cpp")
        // set options
        codeEditor.setOptions({
            // fontFamily:'Inconsolata',
            // fontSize:'12pt',
            enableBasicAutocompletion: true,
            enableLiveAutocompletion: true,

        })
    }
}

function ecxvalues() {
    let z = codeEditor.getValue();
    // console.log(z);
    // console.log(z);
    document.getElementById("w3revi").textContent = z;
}


editorLib.init();
function changeMode() {
    var x = document.getElementById("mode");
    var modeValue = x.options[x.selectedIndex].value;
    if (modeValue == "c") {
        codeEditor.session.setMode("ace/mode/c_cpp");
        checkcc();
        // codeEditor.setValue("#include <stdio.h>\n\n\nint main() {\n    // Complete the code.\n    return 0;\n}\n");
        // codeEditor.clearSelection();
        // document.getElementById('langExt').innerHTML = "c";

    }
    if (modeValue == "cpp") {
        codeEditor.session.setMode("ace/mode/c_cpp");
        checkcc();
        // codeEditor.setValue("#include <iostream>\nusing namespace std;\n\nint main() {\n    // Complete the code.\n    return 0;\n}\n");
        // codeEditor.clearSelection();
        // document.getElementById('langExt').innerHTML = "cpp";

    }
    // if (modeValue == "python2") {
    //     codeEditor.session.setMode("ace/mode/python");
    //     codeEditor.setValue("# Enter your code here. Read input from STDIN. Print output to STDOUT");
    //     codeEditor.clearSelection();
    //     document.getElementById('langExt').innerHTML = "py";
    // }
    if (modeValue == "py") {
        codeEditor.session.setMode("ace/mode/python");
        checkcc();
        // codeEditor.setValue("# Enter your code here. Read input from STDIN. Print output to STDOUT");
        // codeEditor.clearSelection();
        // document.getElementById('langExt').innerHTML = "py";

    }
    // if (modeValue == "java") {
    //     codeEditor.session.setMode("ace/mode/java");
    //     codeEditor.setValue("import java.io.*;\n\nclass Main {\n\n    public static void main(String[] args) {\n        // Your code goes here\n   }\n}\n");
    //     codeEditor.clearSelection();
    //     document.getElementById('langExt').innerHTML = "java";
    // }
}


function ecxvalues() {
    let z = codeEditor.getValue();
    // console.log(z);

    // console.log(z);
    document.getElementById("w3revi").textContent = z;
}


function darkmode() {
    codeEditor.setTheme("ace/theme/tomorrow_night");
    document.getElementById('lightmodebtn').style.display = "inline-block";
    document.getElementById('darkmodebtn').style.display = "none";
}

function lightmode() {
    codeEditor.setTheme("ace/theme/solarized_light");
    document.getElementById('darkmodebtn').style.display = "inline-block";
    document.getElementById('lightmodebtn').style.display = "none";
}


var input = document.getElementById("inputFile");
var output = document.getElementById("editorCode");


// input.addEventListener("change", function () {
//     if (this.files && this.files[0]) {
//         var myFile = this.files[0];
//         var reader = new FileReader();

//         reader.addEventListener('load', function (e) {
//             output.textContent = e.target.result;
//         });

//         reader.readAsBinaryString(myFile);
//     }
// });

document.getElementById("inputFile").addEventListener("change", function () {
    var fr = new FileReader();
    fr.onload = function () {
        //   document.getElementById('editor').textContent=fr.result;
        codeEditor.setValue(fr.result);
        //   alert(fr.result);
    };

    fr.readAsText(this.files[0]);
})