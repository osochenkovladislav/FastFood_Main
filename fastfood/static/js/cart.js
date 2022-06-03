$(document).ready(function() {

    $('#gallery').on('click', '.add-to-cart-btn', (event) => {
        const user_id = $('#user_id').val();
        if (user_id == 'None') {
            alert('Для використання корзини Ви повинні авторизуватись');
            window.location = '/accounts/sign_in';
        }
        else {
            let product_id = $(event.target).prev().val();
            let price = $(event.target).parent().prev().find('h4').text();

            $.ajax({
                url: '/menu/ajax_cart',
                data: `uid=${user_id}&pid=${product_id}&price=${parseFloat(price)}`,
                success: (result) => {
                    $('#count').text(` Кошик ${result.count} шт.`);
                    const user_id = $('#user_id').val();
                }
            });
        }
    });

});