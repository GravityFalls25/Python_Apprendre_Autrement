import mock
with mock.patch("builtins.input", side_effect=['']):
    
    print("Je vais bien")
