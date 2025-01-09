/*
* @name Twitter Bootstrap Show Password
* @descripton
* @version 0.6
* @requires Jquery 1.8.1
*
* @author Jeroen van Meerendonk
* @author-email jeroen@cyneek.com
* @author-website http://cyneek.com
*
* @author Joseba Juániz
* @author-email joseba@cyneek.com
* @author-website http://cyneek.com
* @licens MIT License - http://www.opensource.org/licenses/mit-license.php
*/
(function($){
$.fn.extend({
showPassword: function() {
    var input_password	= $(this);
    var p = input_password.attr('type') == 'password';
    //create the icon and assign
    var icon_password = $('<span tabindex="100" class="input-group-addon password-toggle"><i class="fa fa-eye' + (p ? '' : '-slash') + '"></i></span>').css('cursor', 'help');

    icon_password.on('click', function() {
        if (input_password.attr('type') == 'password') {
            input_password.attr('type', 'text');
            icon_password.find('i').removeClass('fa-eye').addClass('fa-eye-slash');
        } else {
            input_password.attr('type', 'password');
            icon_password.find('i').removeClass('fa-eye-slash').addClass('fa-eye');
        }
    });
    // Create the wrap and append the icon
    input_password.wrap('<div class="input-group" />').before(icon_password);

        }
    });
})(jQuery);
