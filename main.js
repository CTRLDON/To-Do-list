const btn = document.getElementById("add"); // this is the button variable

function addTask()
// add task function, this function will let you input the tasks
{
    const input = document.getElementById("task-input");
    console.log(input.value);
}

btn.addEventListener("click" , addTask);

