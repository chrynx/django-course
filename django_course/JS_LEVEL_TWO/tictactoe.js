$(() => {
  let isXTurn = true;
  const $td = $('td');
  $td.on('click', (e) => {
    if(isXTurn === true){
      $(e.target).text('X');
    } else if(isXTurn === false){
      $(e.target).text('O');
    }
    isXTurn = !isXTurn;
  });
  $('#resetButton').on('click', () => {
    $td.text('');
  });









// =======END========
});
