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


editorLib.init();
function changeMode() {
    var x = document.getElementById("mode");
    var modeValue = x.options[x.selectedIndex].value;
    if (modeValue == "c") {
        codeEditor.session.setMode("ace/mode/c_cpp");
        codeEditor.setValue("#include <stdio.h>\n\n\nint main() {\n    // Complete the code.\n    return 0;\n}\n");
        codeEditor.clearSelection();
        document.getElementById('langExt').innerHTML = "c";
    }
    if (modeValue == "c++") {
        codeEditor.session.setMode("ace/mode/c_cpp");
        codeEditor.setValue("#include <iostream>\nusing namespace std;\n\nint main() {\n    // Complete the code.\n    return 0;\n}\n");
        codeEditor.clearSelection();
        document.getElementById('langExt').innerHTML = "cpp";
    }
    if (modeValue == "python2") {
        codeEditor.session.setMode("ace/mode/python");
        codeEditor.setValue("# Enter your code here. Read input from STDIN. Print output to STDOUT");
        codeEditor.clearSelection();
        document.getElementById('langExt').innerHTML = "py";
    }
    if (modeValue == "python3") {
        codeEditor.session.setMode("ace/mode/python");
        codeEditor.setValue("# Enter your code here. Read input from STDIN. Print output to STDOUT");
        codeEditor.clearSelection();
        document.getElementById('langExt').innerHTML = "py";
    }
    if (modeValue == "java") {
        codeEditor.session.setMode("ace/mode/java");
        codeEditor.setValue("import java.io.*;\n\nclass Main {\n\n    public static void main(String[] args) {\n        // Your code goes here\n   }\n}\n");
        codeEditor.clearSelection();
        document.getElementById('langExt').innerHTML = "java";
    }
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
// var editor = ace.edit("editor");
// // editor.setTheme("ace/theme/monokai");
// editor.setTheme("ace/theme/twilight");

// //editor.setTheme("ace/theme/xcode");
// editor.session.setMode("ace/mode/javascript");
// editor.resize();

// codeeditor.setOptions({
//     enableBasicAutocompletion: true,
//     enableSnippets: true,
//     enableLiveAutocompletion: true,
//     readOnly: false
// });
// $('#myModal').on('shown.bs.modal', function () {
//     $('#myInput').trigger('focus')
//   })

//   function darkmode(){
//       editor.setTheme("ace/theme/monokai");
//       document.getElementById('lightmodebtn').style.display = "inline-block";
//       document.getElementById('darkmodebtn').style.display = "none";
//   }

//   function lightmode(){
//     editor.setTheme("ace/theme/xcode");
//     document.getElementById('darkmodebtn').style.display = "inline-block";
//     document.getElementById('lightmodebtn').style.display = "none";
// }


// const readFile = document.getElementById('choose');
// const inputBtn = document.getElementById('inputFile;');
// const editor = document.getElementById('editorCode');

// readFile.addEventListener('click',addFile);

// function addFile(){
//     // inputBtn.click();
// }

// inputBtn.addEventListener('change',copyText)

// function copyText(){
//     var fr=new FileReader();
//     fr.onload=function(){
//         document.getElementById('editorCode')
//                 .textContent=fr.result;
//     }

//     fr.readAsText(this.files[0]);
// }



// let input = document.querySelector('inputFile')

// let textarea = document.querySelector('questions')

// // This event listener has been implemented to identify a
// // Change in the input section of the html code
// // It will be triggered when a file is chosen.
// input.addEventListener('change', () => {
//     let files = input.files;

//     if (files.length == 0) return;

//     /* If any further modifications have to be made on the
//        Extracted text. The text can be accessed using the 
//        file variable. But since this is const, it is a read 
//        only variable, hence immutable. To make any changes, 
//        changing const to var, here and In the reader.onload 
//        function would be advisible */
//     const file = files[0];

//     let reader = new FileReader();

//     reader.onload = (e) => {
//         const file = e.target.result;

//         // This is a regular expression to identify carriage 
//         // Returns and line breaks
//         const lines = file.split(/\r\n|\n/);
//         textarea.value = lines.join('\n');

//     };

//     reader.onerror = (e) => alert(e.target.error.name);

//     reader.readAsText(file);
// });


var input = document.getElementById("inputFile");
var output = document.getElementById("editorCode");


input.addEventListener("change", function () {
    var fr = new FileReader();
    fr.onload = function () {
        //   document.getElementById('editor').textContent=fr.result;
        editor.setValue(fr.result);
        //   alert(fr.result);
    };

    fr.readAsText(this.files[0]);
});