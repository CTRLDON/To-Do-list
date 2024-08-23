const btn = document.getElementById("add"); // this is the button variable
const input = document.getElementById("task-input"); // this is input field constant
var i = 1

function addTask(){
// add task function, this function will let you input the tasks
// this is a new note
    const x = i;
    var text = input.value;
    const newDiv = document.createElement("div");
    newDiv.className = `task task${x}`;
    // newDiv.innerText = text;
    const deleteBtn = document.createElement("button");
    deleteBtn.className = `task${x} delete`;
    deleteBtn.innerHTML = "Delete";
    deleteBtn.onclick = function(){
        document.querySelector(`.task.${deleteBtn.classList[0]}`).remove();
    };
    const taskText = document.createElement("p");
    taskText.className = "text";
    taskText.innerHTML = text;
    const finishedBtn = document.createElement("button");
    finishedBtn.className = `done${x} finished`;
    finishedBtn.innerHTML = "Finished";
    finishedBtn.onclick = function(){
        document.querySelector(`.task.${finishedBtn.classList[0]}`).remove();
    };
    newDiv.appendChild(finishedBtn);
    newDiv.appendChild(taskText);
    newDiv.appendChild(deleteBtn);
    document.body.appendChild(newDiv);
    i++;
}

btn.addEventListener("click" , addTask);
document.addEventListener("keypress",function(event){
    if(event.key == 'Enter'){
        event.preventDefault();
        addTask();
    }
});

