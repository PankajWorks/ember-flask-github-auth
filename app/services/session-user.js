import Ember from 'ember';

export default Ember.Service.extend({
    session: Ember.inject.service(),
    store: Ember.inject.service(),
    loadCurrentUser() {
        return new Ember.RSVP.Promise((resolve, reject) => { 
          if(this.get('session.isAuthenticated')){
            this.get('store').findRecord('github-user', '#').then((user)=>{
                resolve();
                let _detail = {
                    'name':user.get('name'),
                    'login':user.get('login'),
                    'avatarUrl':user.get('avatarUrl')
                }
                this.set('user',_detail);
            }, reject);
        } else {
            resolve();
        }
        });
      }
});
