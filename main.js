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
    newDiv.innerHTML = text;
    const deleteBtn = document.createElement("button");
    deleteBtn.className = `task${x}`;
    deleteBtn.innerHTML = "Delete";
    deleteBtn.onclick = function(){
        document.querySelector(`.task.${deleteBtn.getAttribute("class")}`).remove();
    };
    newDiv.appendChild(deleteBtn);
    document.body.appendChild(newDiv);
}

btn.addEventListener("click" , addTask);
document.addEventListener("keypress",function(event){
    if(event.key == 'Enter'){
        event.preventDefault(); 
        addTask();
    }
});

