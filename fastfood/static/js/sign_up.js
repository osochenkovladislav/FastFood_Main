$(document).ready(() => {

   console.log('jQuery-OK');
   let validateResult1 = false;  //- результат валідації 1 пароля
   let validateResult2 = false;  //- результат валідації 2 пароля
   let validateResult3 = false;  //- результат валідації email

   // 1. Валідація 1 пароля:
   // ----------------------
   $('#pass1').blur(() => {
        let pass1X = $('#pass1').val();
        let passRe = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[_\-])[a-zA-Z0-9_\-]{8,}$/;

        console.log(pass1X);
        if (passRe.test(pass1X)) {
            $('#pass1_err').text('');
            validateResult1 = true;
        } else {
            $('#pass1_err').text('Пароль має містити хоча б одну головну букву, цифру та спеціальний знак');
            validateResult1 = false;
        }
   });

   // 2. Валідація 2 пароля:
   // ----------------------
   $('#pass2').blur(() => {
        let pass1X = $('#pass1').val();
        let pass2X = $('#pass2').val();

        console.log(pass1X + ' / ' + pass2X);
        if (pass1X === pass2X) {
            $('#pass2_err').text('');
            validateResult2 = true;
        } else {
            $('#pass2_err').text('Введені паролі не співпадають');
            validateResult2 = false;
        }
   });

   // 3. Валідація e-mail
   // -------------------
   $('#email').blur(() => {
        let emailX = $('#email').val();
        let emailRe = /^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$/;

        console.log(emailX);
        if (emailRe.test(emailX)) {
            $.ajax({
                url: '/accounts/ajax_email',
                data: 'email=' + emailX,
                success: (result) => {
                    if (result.message === 'зайнятий') {
                     $('#email_err').text('E-Mail - зайнятий!  Спробуйтк інший');
                     validateResult3 = false;
                    } else {
                        $('#email_err').text('');
                        validateResult3 = true;
                    }
                }
            });
        } else {
            $('#email_err').text('Введіть коректний E-Mail');
            validateResult3 = false;
        }
   });


   $('#submit').click(() => {
        if (validateResult1 === true && validateResult2 === true && validateResult3 === true) {
            $('#form-1').attr('onsubmit', 'return true');
        } else {
            $('#form-1').attr('onsubmit', 'return false');
            alert('Форма містить некоректні дані!\nВідправка даних заблокована!');
        }
   })
});