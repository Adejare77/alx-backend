const kue = require('kue');
const jobs = kue.createQueue();

const jobData = {
  phoneNumber: '2348148965657',
  message: 'This is the code to verify your account'
};

const job = jobs.create('push_notification_code', jobData)
  .save((err) => {
    if (err) {
      console.error('Notification job failed');
      return;
    }
    console.log(`Notification job created: ${job.id}`);
  });

function sendNotification (phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// Add event listeners to listen on completion or failure
job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', (err) => {
  console.error('Notification job failed:', err);
});

// Add queue process to listen for new jobs (1 job at a time by default)
jobs.process('push_notification_code', (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message);
  done();
});
