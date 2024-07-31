const kue = require('kue');
const queue = kue.createQueue();

const blackListedPhoneNumbers = [4153518780, 4153518781];

function sendNotification (phoneNumber, message, job, done) {
  // Arbitrary checkpoint reporting to me on where I am. This is for reporting purpose
  // So, I decided to call this point to be 1000% completed out of 100%
  job.progress(0, 100);

  if (blackListedPhoneNumbers.includes(phoneNumber)) {
    job.fail(new Error(`Phone number ${phoneNumber} is blacklisted`));
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  // Arbitrary checkpoint reporting to me  where I'm currently at.
  // So, I tracked it to be 50% completed out of 100%
  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done(); // Indicate job complete
}

// Proceed with two jobs at a time (concurrently), thus the '2'
queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
