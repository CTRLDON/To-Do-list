const btn = document.getElementById("add"); // this is the button variable

function addTask() {
    const input = document.getElementById("task-input");
    console.log(input.value);
}

btn.addEventListener("click" , addTask);

