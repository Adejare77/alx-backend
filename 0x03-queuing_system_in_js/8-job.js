function createPushNotificationsJobs (jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }
  for (const job of jobs) {
    let queuedJob = queue.create('push_notification_code_3', job)
      .save((err) => {
        if (err) {
          console.log(`Notification job failed: ${err}`);
          return;
        }
        console.log(`Notification job created: ${queuedJob.id}`);
      });

    // When the job completes on 'execution'
    queuedJob.on('complete', () => {
      console.log(`Notification job ${queuedJob.id} completed`);
    });

    // Job progress during 'execution'
    queuedJob.on('progress', (progress) => {
      console.log(`Notification job ${queuedJob.id} ${progress}% complete`);
    });
  }
}

module.exports = createPushNotificationsJobs;
