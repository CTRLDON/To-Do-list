const btn = document.getElementById("add"); // this is the button variable

function addTask()
// add task function, this function will let you input the tasks
// this is a new note
{
    const input = document.getElementById("task-input"); // this is input field constant
    console.log(input.value);
}

btn.addEventListener("click" , addTask);

