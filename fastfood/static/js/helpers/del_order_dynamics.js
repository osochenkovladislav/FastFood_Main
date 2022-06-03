export const delOrderDynamics = () => {

      const user_id = $('#user_id').val();
      $.ajax({
            url: '/accounts/ajax_del_order_dynamics',
            data: `uid=${user_id}`,
            success: (result) => {

            let code = '';
            for (let order of result.orders) {
                            code += `
                              <div class="item">
                                  <div class="buttons">
                                      <input type="hidden" value=${order.id}>
                                      <span class="delete-btn"></span>
                                      <span class="like-btn"></span>
                                  </div>
                                  <div class="photoBorder" style="align=center;">
                                      <img align="center" src="/media/${order.picture}" alt="" class="photoImage"/>
                                  </div>
                                  <div class="description">
                                      <span>${order.name}</span>
                                  </div>
                                  <div class="price_cell" >${order.amount} грн</div>
                              </div>
                            `;
                        }
                    $('#cart-item').html(code);

                    let priceCells = $('.price_cell');
                    let totalPrice = 0;
                    for (let cell of priceCells) {
                        totalPrice += parseFloat($(cell).text());
                    }
                    console.log(`totalPrice = ${totalPrice}`);
                    $('#total').text(`${totalPrice.toFixed(2)} грн.`)

                }
            });
};