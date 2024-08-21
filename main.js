let btn = document.getElementById("add"); // Button for the code

function addTask() {
    let input = document.getElementById("task-input");
    console.log(input.value);
}

btn.onclick = addTask();

