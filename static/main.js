const btn = document.getElementById("add"); // this is the button variable
const input = document.getElementById("task-input"); // this is input field constant
var i = 1

function addTask(){
// add task function, this function will let you input the tasks
// this is a new note
    const x = i;
    var text = $('#task-input').val();
    console.log(text)
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
    const finishedBtn = document.createElement("a");
    finishedBtn.className = `done${x} finished`;
    finishedBtn.innerHTML = "Finished";
    finishedBtn.href = '/addtask'
    finishedBtn.onclick = function(){
            $.ajax({
                url : "/addtask",
                type : "POST",
                data : {
                    'info' : text
                },
                success : function(response) {
                    alert("success");
                },
                error: function(error) {
                    console.log('Error:', error);
                }
            });
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
