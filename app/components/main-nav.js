import Ember from 'ember';

export default Ember.Component.extend({
    session: Ember.inject.service(),
    sessionUser: Ember.inject.service(),
    // Inject a service to get account information

    actions: {
        login(){
            this.get('session').authenticate('authenticator:torii', 'github');
        },

        logout(){
            this.get('session').invalidate();
        }
    }
});
