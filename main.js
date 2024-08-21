const btn = document.getElementById("add");

function addTask() {
    const input = document.getElementById("task-input");
    console.log(input.value);
}

btn.addEventListener("click" , addTask);

