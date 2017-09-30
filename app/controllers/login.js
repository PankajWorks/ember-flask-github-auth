import Ember from 'ember';

export default Ember.Controller.extend({
    session: Ember.inject.service(),
    sessionUser: Ember.inject.service(),
    
      actions: {
    
        authenticateWithGithub() {
            this.get('session').authenticate('authenticator:torii', 'github');
        },
    
        
      }
});
