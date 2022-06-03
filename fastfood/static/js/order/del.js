import { delOrderDynamics } from '../../js/helpers/del_order_dynamics.js';
import { cartDynamics } from '../../js/helpers/cart_dynamics.js';

$(document).ready(() => {

    console.log('del_order - start')

    $('#cart-item').on('click', '.delete-btn', (event) => {

        console.log('delete-btn - click')

        let order_id = $(event.target).prev().val();
        console.log(`order_id - ${order_id}`);

        $.ajax({
            url: '/accounts/ajax_del_order',
            data: `order_id=${order_id}`,
            success: (result) => {
                   console.log(result.message)
                   delOrderDynamics();
                   cartDynamics();
                }

        });
    });

});
