$(function() {
  var imgList = [
    '1.jpg',
    '2.jpg',
    '3.jpg',
    '4.jpg',
    '5.jpg',
    '6.jpg'
  ], i = 0, $img = $('#img_slider'), imgPath = 'static/img/', $errorHandler = $('#form_errors'), $headerText = $('#header_text'),
  $firstLink = $('ul.user-link > li > a').eq(0), $container = $('#container');

  function setSrc() {
    $img.attr('src', imgPath + imgList[i]);
    if (i < imgList.length - 1) {
      i++;
    }
    else {
      i = 0;
    }
    setTimeout(function() { setSrc(); }, 2000);
  }

  function editUserBind() {
    var $cancleBtn = $('#edit_user_cancel').click(function(e) {
      e.preventDefault();
      if ($firstLink.length > 0) {
        $firstLink.click();
      }
    });
    $('#edit_user_form').validate({
      rules: {
        first_name: {
          required: true
        },
        last_name: {
          required: true
        },
        email: {
          required: true,
          email: true
        },
        group: {
          required: true
        },
        manager: {
          required: true
        }
      },
      messages: {
        first_name: {
          required: '*'
        },
        last_name: {
          required: '*'
        },
        email: {
          required: '*',
          email: '*'
        },
        group: {
          required: '*'
        },
        manager: {
          required: '*'
        }
      },
      submitHandler: function (form) {
        $.ajax({
          url: form.action,
          type: form.method,
          data: $(form).serialize(),
          cache: false,
          success: function(response) {
            if (0 == response.status) {
              $('#form_error').text(response.message).show();
            }
            else {
              $cancleBtn.click();
              alert(response.message);
            }
          },
          error: function(jqXHR, textStatus, errorThrown) {
            console.log('ERRORS: ' + textStatus);
          }
        });
      }
    });
  }
  function addUserBind() {
    var $cancleBtn = $('#add_user_cancel').click(function(e) {
      e.preventDefault();
      if ($firstLink.length > 0) {
        $firstLink.click();
      }
    });
    $('#add_user_form').validate({
      rules: {
        first_name: {
          required: true
        },
        last_name: {
          required: true
        },
        email: {
          required: true,
          email: true
        },
        password: {
          required: true
        },
        group: {
          required: true
        },
        manager: {
          required: true
        }
      },
      messages: {
        first_name: {
          required: '*'
        },
        last_name: {
          required: '*'
        },
        email: {
          required: '*',
          email: '*'
        },
        password: {
          required: '*'
        },
        group: {
          required: '*'
        },
        manager: {
          required: '*'
        }
      },
      submitHandler: function (form) {
        $.ajax({
          url: form.action,
          type: form.method,
          data: $(form).serialize(),
          cache: false,
          success: function(response) {
            if (0 == response.status) {
              $('#form_error').text(response.message).show();
            }
            else {
              $cancleBtn.click();
              alert(response.message);
            }
          },
          error: function(jqXHR, textStatus, errorThrown) {
            console.log('ERRORS: ' + textStatus);
          }
        });
      }
    });
  }


  function bookCabBind() {
    var $bookingLink = $('.booking-link'), $bookingDiv = $('.be-ex');
    if ($bookingLink.length > 0) {
      $bookingLink.click(function(e) {
        e.preventDefault();
        var $this = $(this);
        $bookingLink.parent().removeClass('active');
        $this.parent().addClass('active');
        $bookingDiv.hide();
        $($this.attr('href')).show();
      });
      $bookingLink.eq(0).click();
    }
  }

  if ($img.length > 0) {
    setSrc();
  }
  $('#login_form').validate({
    rules: {
      email: {
        required: true
      },
      password: {
          required: true
      }
    },
    messages: {
      email: {
        required: '*'
      },
      password: {
        required: '*'
      }
    },
    submitHandler: function (form) {
      $.ajax({
        url: form.action,
        type: form.method,
        data: $(form).serialize(),
        cache: false,
        success: function(response) {
          if (1 === response.status) {    // success
            top.location.href = response.url;
          }
          else {      // error
            $errorHandler.html(response.message);
            $errorHandler.show();
          }
        },
        error: function(jqXHR, textStatus, errorThrown) {
          console.log('ERRORS: ' + textStatus);
        }
      });
    }
  });
  $('#add_user').click(function(e){
    e.preventDefault();
    $headerText.text("Add User");
    $container.empty();
    $.ajax({
      url: '/add-user/',
      type: 'get',
      cache: false,
      success: function(response) {
        $container.html(response.html);
        addUserBind();
      },
      error: function(jqXHR, textStatus, errorThrown) {
        console.log('ERRORS: ' + textStatus);
      }
    });
  });
  $('#view_users').click(function(e){
    e.preventDefault();
    $headerText.text("Users");
    $container.empty();
    $.ajax({
      url: '/get-users/',
      type: 'get',
      cache: false,
      success: function (response) {
        if (1 === response.status) {    // success
          var $table = $('<table/>').addClass('user-table'), $tr = $('<tr/>'), $td;
          $('<th/>').text('S.No.').appendTo($tr);
          $('<th/>').text('Name').appendTo($tr);
          $('<th/>').text('Username (Emp ID)').appendTo($tr);
          $('<th/>').text('Email').appendTo($tr);
          $('<th/>').text('Group').appendTo($tr);
          $('<th/>').text('Manager').appendTo($tr);
          $('<th/>').text('Action').appendTo($tr);
          $tr.appendTo($table);
          for (var i = 0, ln = response.data.length; i < ln; i++) {
            $tr = $('<tr/>');
            $('<td/>').text(response.data[i][0]).appendTo($tr);
            $('<td/>').text(response.data[i][1] + " " + response.data[i][2] ).appendTo($tr);
            $('<td/>').text(response.data[i][3]).appendTo($tr);
            $('<td/>').text(response.data[i][4]).appendTo($tr);
            $('<td/>').text(response.data[i][5]).appendTo($tr);
            $('<td/>').text(response.data[i][6]).appendTo($tr);
            $td = $('<td/>')
            $('<a/>').data('user_id', response.data[i][8]).html('<span class="icon_i"><i class="fa fa-edit fa fw"></i></span>').attr('href', '#').click(function(e) {
              e.preventDefault();
              var user_id = $(this).data('user_id');
              $.ajax({
                url: '/edit-user/',
                data: {'user_id': user_id},
                type: 'get',
                cache: false,
                success: function(response) {
                  if (response.status == 0) {
                    alert(response.message);
                  }
                  else {
                    $headerText.text("Edit User");
                    $container.html(response.html);
                    editUserBind();
                  }
                }
              });
            }).appendTo($td);
            if (response.data[i][7] == true) {
              $('<a/>').data('user_id', response.data[i][8]).html('<span class="icon_i"><i class="fa fa-trash-o fa fw"></i></span>').attr('href', '#').click(function(e) {
                e.preventDefault();
                var user_id = $(this).data('user_id');
                if (confirm('Are you sure, You want to delete this user?')) {
                  $.ajax({
                    url: '/delete-user/',
                    type: 'get',
                    data: {'user_id': user_id},
                    cache: false,
                    success: function(response) {
                      if (response.status = 0) {
                        alert(response.message);
                      }
                      else {
                        alert(response.message);
                        if ($firstLink.length > 0) {
                          $firstLink.click();
                        }
                      }
                    }
                  });
                };
              }).appendTo($td);
            }
            $td.appendTo($tr);
            $tr.appendTo($table);
          }
          $table.appendTo($container);
        }
        else {
          var $div = $('<div/>').addClass('alert_icons_block');
          $('<div/>').addClass('box error').text(response.message).appendTo($div);
          $div.appendTo($container);
        }
      },
      error: function(jqXHR, textStatus, errorThrown) {
        console.log('ERRORS: ' + textStatus);
      }
    });
  });
  $('#book_cab').click(function(e) {
    e.preventDefault()
    $headerText.text('Book Cab');
    $.ajax({
      url: '/employee/cab-booking/',
      type: 'get',
      cache: false,
      success: function(response) {
        if (response.status = 1) {
          $container.html(response.html);
          bookCabBind();
        }
        else {
          $("<label/>").addClass('error').text(response.message).appendTo($container.empty());
        }
      }
    });
    
  });
  $('#view_cab').click(function(e) {
    e.preventDefault()
    $headerText.text('View Cabs');
    $container.html('You can view your cab');
  });
  $('#approve_cab').click(function(e) {
    e.preventDefault()
    $headerText.text('Approve Cabs');
    $container.html('You can approve your employees cab');
  });
  if ($firstLink.length > 0) {
    $firstLink.click();
  }
});