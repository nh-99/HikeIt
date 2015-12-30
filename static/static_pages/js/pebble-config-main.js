(function() {
  submitHandler();
})();

function submitHandler() {
  var $submitButton = $('#submitButton');

  $submitButton.on('click', function() {
    console.log('Submit');
    var return_to = getQueryParam('return_to', 'pebblejs://close#');
    getAndStoreConfigData(function(options) {
          document.location = return_to + encodeURIComponent(JSON.stringify(options));
        });
  });
}

function getAndStoreConfigData(callback) {
  var username = $('#username').val();
  var password = $('#password').val();
  
  var token = "blah";
  token = login(username, password, function(token) {
        var options = {
    token: token
  };

  localStorage.token = options.token;

  console.log('Got options: ' + JSON.stringify(options));
  callback(options);
      });
}

function getQueryParam(variable, defaultValue) {
  var query = location.search.substring(1);
  var vars = query.split('&');
  for (var i = 0; i < vars.length; i++) {
    var pair = vars[i].split('=');
    if (pair[0] === variable) {
      return decodeURIComponent(pair[1]);
    }
  }
  return defaultValue || false;
}

function login(user, pass, callback) {
  var req = $.ajax({
    type: 'POST',
    beforeSend: function(xhr) {
      xhr.setRequestHeader('Authorization', "Basic " + window.btoa(user + ":" + pass));
    },
    data: {
      "username": user,
      "password": pass
    },
    url: 'https://hikeit.me/user/token/',
    crossDomain: true,
    dataType: 'json',
    success: function(res) {
        console.log(res);
        callback(res.token);
    },
    error: function(res) {
        console.log(res);
    }
  });
}

