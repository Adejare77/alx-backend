import { describe, it, before, after, afterEach } from 'mocha';
import { expect } from 'chai';
import { createQueue } from 'kue';

import createPushNotificationsJobs from './8-job.js';

const queue = createQueue();

describe('Test createPushNotificatinsJobs function', function() {
  before(function () {
    queue.testMode.enter();
  });

  afterEach(function () {
    queue.testMode.clear();
  });

  after(function () {
    queue.testMode.exit();
  });

  it('display an error message if jobs is not an array', function() {
    expect(() => createPushNotificationsJobs('job', queue)).to.throw(Error, 'Jobs is not an array');
  });

  it('Test whether jobs are created', function() {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account'
      },
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(2);

    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.eql(jobs[0]);

    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].data).to.eql(jobs[1]);
  });
});


// describe('createPushNotificationsJobs', () => {
//   let queue;

//   beforeEach(() => {
//     // creating new queue elps in maintaining test isolation and reliability
//     // thus, error from one won't impact others
//     queue = kue.createQueue();
//     queue.testMode.enter();
//   });

//   afterEach(() => {
//     queue.testMode.clear()
//   });

//   after(() => {
//     queue.testMode.exit();
//   })

//   it('Create Job and add them to the queue', () => {
//     const jobs = [{ phoneNumber: '1234567890', message: 'Test message' }];
//     // spy on the output to be produced in console
//     const consoleSpy = sinon.spy(console, 'log');

//     createPushNotificationsJobs(jobs, queue);

//     // Verify that the job is added to the queue
//     const queuedJobs = queue.testMode.jobs;
//     chai.expect(queuedJobs).to.have.lengthOf(1);
//     console.log('-----------------------------')
//     console.log(queue.testMode.jobs)
//     console.log(console.log(queuedJobs))
//     console.log('-----------------------------')
//     // chai.expect(consoleSpy).to.include('Notification job');
//     consoleSpy.restore();
//   })
// });
