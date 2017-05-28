exports.handler = (event, context, callback) => {
  // process GET request
  if (event.params && event.params.querystring) {
    var queryParams = event.params.querystring;
 
    var rVerifyToken = queryParams['hub.verify_token'];
 
    if (rVerifyToken === VERIFY_TOKEN) {
      var challenge = queryParams['hub.challenge'];
      callback(null, parseInt(challenge));
    } else {
      callback(null, 'Error, wrong validation token');
    }
 
  // process POST request
  } else {
    var messagingEvents = event.entry[0].messaging;
    for (var i = 0; i < messagingEvents.length; i++) {
      var messagingEvent = messagingEvents[i];
 
      console.log("Received a message event:", JSON.stringify(messagingEvent, null, 2));
      if (messagingEvent.message && !messagingEvent.message.is_echo) {
        var sender = messagingEvent.sender.id;
        getConversation(sender).then(function(data) {
          console.log("Stored conversation:", JSON.stringify(data, null, 2));
            
          var conversation = data.Item;
          // Is known?
          if (conversation) {
            // Is known: yes
            // If message contains text echo it, otherwise send a thumbs up
            var messageText = "\ud83d\udc4d";
            if (messagingEvent.message.text) {
              conversation.lastMessage = messagingEvent.message.text;
              messageText = "Text received, echo: " +
                messagingEvent.message.text.substring(0, 200);
            }
            
            return {
              conversation: conversation,
              messageData: createTextMessageData(sender, messageText),
              updateDB: conversation.hasJoined
            };
          } else {
            // Is known: no
            return processJoinMessage(messagingEvent.message, sender);
          }
        }).then(function(result) {
        if (result.messageData) {
            callSendAPI(result.messageData);
        }
          
          return result;
      }).then(function(result) {
          if (result.updateDB) {
          console.log("There is an update to store:", JSON.stringify(result.conversation, null, 2));
          return putConversation(result.conversation);
        }
      }).catch(function(error) {
        console.error("Error:", JSON.stringify(error, null, 2));
        });
        
        callback(null, "Done");
      }
    }
 
    callback(null, event);
  }
};