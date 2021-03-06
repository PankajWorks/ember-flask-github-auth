import Ember from 'ember';
import ApplicationRouteMixin from 'ember-simple-auth/mixins/application-route-mixin';

export default Ember.Route.extend(ApplicationRouteMixin,{
    sessionUser: Ember.inject.service('session-user'),
    
      beforeModel() {
        return this._loadCurrentUser();
      },
    
      sessionAuthenticated() {
        this._super(...arguments);
        this._loadCurrentUser();
      },
    
      _loadCurrentUser() {
        return this.get('sessionUser').loadCurrentUser().catch(() => this.get('session').invalidate());
      }
});

