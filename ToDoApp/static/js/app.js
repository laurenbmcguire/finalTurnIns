

let form = document.querySelector('#todoForm');
let ul = document.querySelector('#todoList');

form.addEventListener('submit', e => {
    e.preventDefault();

    let li = document.createElement('li');
    li.classList.add('list-group-item');
    li.innerText = e.target.todoItemInput.value;
    li.addEventListener('mouseenter', (e) => li.classList.add('active'));
    li.addEventListener('mouseleave', e => li.classList.remove('active'))
    li.addEventListener('click', (e) => {
        if(li.classList.contains('disabled')){
            li.classList.remove('disabled');
            li.classList.add('active');
            li.style.textDecoration = 'none';
        } else if(li.classList.contains('active')) {
            li.classList.remove('active');
            li.classList.add('disabled');
            li.style.textDecoration = 'line-through'
        }
        console.log("sup")
    })
    ul.appendChild(li)
    e.target.todoItemInput.value = '';
})
let clearbutton = document.querySelector('#clear');
clearbutton.addEventListener('click', e => {
    e.preventDefault();
    ul.innerHTML = "";
})




