const btn = document.getElementById("add"); // this is the button variable
const input = document.getElementById("task-input"); // this is input field constant

function addTask(){
// add task function, this function will let you input the tasks
// this is a new note

    const newDiv = document.createElement("div");
    newDiv.className = `${input.value} task`;
    newDiv.innerHTML = input.value;
    document.body.appendChild(newDiv);
}

btn.addEventListener("click" , addTask);

