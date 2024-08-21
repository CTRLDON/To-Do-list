let btn = document.getElementById("add");

function addTask() {
    let input = document.getElementById("task-input");
    console.log(input.value);
}

btn.onclick = addTask();

