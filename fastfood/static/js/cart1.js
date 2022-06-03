$(document).ready(function() {

    let priceCells = $('.price_cell');
    let totalPrice = 0;
    for (let cell of priceCells) {
        totalPrice += parseFloat($(cell).text());
    }
    console.log(`totalPrice = ${totalPrice}`);
    $('#total').text(`${totalPrice.toFixed(2)} грн.`)

    $('.like-btn').on('click', function() {
       $(this).toggleClass('is-active');
    });

    $('.minus-btn').on('click', function(e) {
        e.preventDefault();
        var $this = $(this);
        var $input = $this.closest('div').find('input');
        var value = parseInt($input.val());

        if (value > 1) {
            value = value - 1;
        } else {
            value = 0;
        }

      $input.val(value);

    });

    $('.plus-btn').on('click', function(e) {
        e.preventDefault();
        var $this = $(this);
        var $input = $this.closest('div').find('input');
        var value = parseInt($input.val());

        if (value < 100) {
            value = value + 1;
        } else {
            value = 100;
        }
        $input.val(value);
        });

});