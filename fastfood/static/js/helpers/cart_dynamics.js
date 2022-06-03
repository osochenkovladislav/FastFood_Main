export const cartDynamics = () => {

    const user_id = $('#user_id').val();

    $.ajax({
        url: '/menu/ajax_cart_display',
        data: `uid=${user_id}`,
        success: (result) => {
            console.log('cart_display work fine');
            console.log(result.amount);
            console.log(result.count);

            $('#count').text(` Кошик ${result.count} шт.`);
        }
    })

};