// Add task button
const button = document.getElementById("add-ID"); 
// Input text
const input = document.getElementById("task-input"); 

var i = ids[0] // the unique ID variable

function addTaskElement(task){
    const x = i;
    const newDiv = document.createElement("div"); // creating a new div container for the task added by the user
    newDiv.className = `task task${x}`; // assigning a class name for the task div container with the unique ID
    // newDiv.innerText = text;
    // ------------------------------------------------------------------------
    // creating the Delete button for the task
    const deleteBtn = document.createElement("button"); // adding a delete button for the task div container
    deleteBtn.className = `task${x} delete`; // assigning a class name for the button using the unique ID
    deleteBtn.innerHTML = "Delete"; // make the value of the button that appears to the user "Delete"
    // deleting the task div container when the delete button get clicked
    deleteBtn.onclick = function(){ 
        deleteTask(deleteBtn.classList[0] , x); //selecting the container using the delete button class name and then removing it 
    };
    //--------------------------------------------------------------------------
    // adding the task name in the container
    const taskText = document.createElement("p"); // creates a paragraph element for the task name
    taskText.className = "text"; // assiging a class for the paragraph element
    taskText.innerHTML = task; // adding the task in the paragraph element (what shows up for the user)
    // ------------------------------------------------------------------------
    // adding a finished button for the task div container 
    const finishedBtn = document.createElement("button"); // creating a link element
    finishedBtn.className = `task${x} finished`; // assiging a class name for it using the unique ID
    finishedBtn.innerHTML = "Finished"; // make the value of the link that appears to the user "Finished"
    // triggering a fucntion on the click of the finished button that creates an api and sends data to the server with text information
    finishedBtn.onclick = function(){
            doneTask(finishedBtn.classList[0],x);
    };
    // ------------------------------------------------------------------------
    newDiv.appendChild(finishedBtn); // adding finished button to task div container
    newDiv.appendChild(taskText); // adding the task text or name to the taks div container
    newDiv.appendChild(deleteBtn); // adding delete button to task div container
    document.body.appendChild(newDiv); // adding task div container to the body of the page
    // ------------------------------------------------------------------------
    i++; // changing the unique ID for the new element to be created
}

function deleteTask(deletebtnClass,id){
    document.querySelector(`.task.${deletebtnClass}`).remove();
    $.ajax({
        url : "/deletetask", //The url that when routed to it will trigger the API
        type : "POST", // makes the type of the API POST meaning that it will going to send data to the server not reading data from the server
        // the data that will be sent
        contentType: "application/json",
        data : JSON.stringify({
            'info' : id
        }),
        // a function that if the process was a success it will be triggered
        success : function(response) {
            console.log(id);
        },
        // a function the if the process was a failure it will be triggered
        error: function(error) {
            console.log('Error:', error);
        }
    });

}

function doneTask(finishedBtnClass,id){
    document.querySelector(`.task.${finishedBtnClass}`).remove();
    $.ajax({
        url : "/donetask", //The url that when routed to it will trigger the API
        type : "POST", // makes the type of the API POST meaning that it will going to send data to the server not reading data from the server
        // the data that will be sent
        contentType: "application/json",
        data : JSON.stringify({
            'id' : id
        }),
        // a function that if the process was a success it will be triggered
        success : function(response) {
            console.log(id);
        },
        // a function the if the process was a failure it will be triggered
        error: function(error) {
            console.log('Error:', error);
        }
    });

}

function loadTasks(){
    console.log(tasks)
    if(tasks.length === 0){ // checking if the data is none
        console.log("nothing");
    }else{ // if the data is not empty : 
        for(let j = 0;j<tasks.length;j++){
            addTaskElement(tasks[j]); // loading each task
        }
    }
}

function addTask(){
    var text = $('#task-input-ID').val(); // getting text from task input field
    addTaskElement(text); // adding the task element
    $.ajax({
        url : "/addtask", //The url that when routed to it will trigger the API
        type : "POST", // makes the type of the API POST meaning that it will going to send data to the server not reading data from the server
        // the data that will be sent
        contentType: "application/json",
        data : JSON.stringify({
            'info' : text
        }),
        // a function that if the process was a success it will be triggered
        success : function(response) {
            console.log(text);
        },
        // a function the if the process was a failure it will be triggered
        error: function(error) {
            console.log('Error:', error);
        }
    });
}

window.onload = function(){ // when the page loads it triggers this function
    loadTasks(); // loading all tasks saved in the database
}

button.addEventListener("click" , addTask); // triggering the addTask function when add task button get clicked
// triggering addTask fucntion when enter button get pressed on the keyboard
document.addEventListener("keypress",function(event){
    if(event.key == 'Enter'){
        event.preventDefault(); // preventing the normal use of the enter button which is creaing new line 
        addTask();
    }
});

