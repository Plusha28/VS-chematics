'use strict';

const e = React.createElement;

class LikeButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = { liked: false };
  }

  render() {
    if (this.state.liked) {
      return 'You liked this.';
    }

    return e(
      'button',
      { onClick: () => this.setState({ liked: true }) },
      'Like'
    );
  }
}

const domContainer = document.querySelector('#like_button_container');
ReactDOM.render(e(LikeButton), domContainer);




let add = document.getElementById('addJSON');
let form = document.getElementById('formAddJSON');

//удаление родительского дива с инпутом при нажатии кнопки удаления
form.addEventListener('click', function(event) {
  document.querySelector('.add-json-form').onclick = function(e) {
  const btn = e.target.closest('.delete-json');
  if (!btn) {
    return;
  }
  btn.parentElement.remove();
}
});

//создание дива с инпутом и кнопкой по клику
//нужно переписать на реакте для динамического обновления формы
// add.addEventListener('click', function(event) {
//   let input = document.createElement('input');
//   input.type = 'file';
//   input.classList.add('form-control-file');
//   input.accept = '.json';
//
//   let span = document.createElement('span')
//   span.textContent = 'Удалить'
//   span.classList.add('delete-json');
//
//
//   let div = document.createElement('div')
//   div.classList.add('add-json-form');
//
//   div.append(span);
//   div.prepend(input);
//   form.insertBefore(div, add);
// });

function AddInput() {
    const input = useState('<input type="file" className="form-control-file" accept=".json" required>');
    const span =  useState('<span className="delete-json">Удалить</span>');
    const div = useState('<div className="add-json-form">{input}{span}</div>');

    ReactDOM.render(
      div,
      document.getElementById('formAddJSON')
    );
}





//удаление последнего снизу дива с инпутом и кнопкой
function removeElement() {
  let jsonFile = document.querySelectorAll('.form-control-file');
  for (let i = 0; i < jsonFile.length; i--)
    jsonFile[i].parentNode.removeChild(jsonFile[i]);
}



function previewFile() {
  let preview = document.getElementById('img');
  let file    = document.getElementById('pct').files[0];
  let reader  = new FileReader();

  reader.onloadend = function () {
    preview.src = reader.result;
  }

  if (file) {
    reader.readAsDataURL(file);
  } else {
    preview.src = "";
  }
}