document.getElementById('spamForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const emailText = document.getElementById('emailText').value;
    const submitBtn = document.getElementById('submitBtn');
    const idleState = document.getElementById('idleState');
    const resultBox = document.getElementById('resultBox');
    const predictionText = document.getElementById('predictionText');
    const confidenceText = document.getElementById('confidenceText');
    const statusPill = document.getElementById('statusPill');
    const meterFill = document.getElementById('meterFill');
    const meterNeedle = document.getElementById('meterNeedle');

    // Set UI to loading state
    submitBtn.querySelector('.btn-label').textContent = 'Scanning…';
    submitBtn.disabled = true;
    statusPill.textContent = 'SCANNING';
    statusPill.className = 'chrome__status is-scanning';

    try {
        const response = await fetch('/api/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            // Matches the PredictionReq schema (req.email_text)
            body: JSON.stringify({ email_text: emailText })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();

        // Adjust this logic based on what your model outputs for `data.prediction`
        // e.g., 1 vs 0, or "spam" vs "ham"
        const isSpam = data.prediction === 1 || String(data.prediction).toLowerCase() === 'spam';
        const confidencePct = (data.confidence * 100).toFixed(1);

        // Position on a safe(0%) -> spam(100%) scale, regardless of which
        // class the model's confidence score was reported against.
        const spamProbability = isSpam ? data.confidence : (1 - data.confidence);
        const meterPct = Math.min(100, Math.max(0, spamProbability * 100));

        // Update result panel
        predictionText.textContent = isSpam ? '🚨 This looks like SPAM' : '✅ This looks SAFE';
        predictionText.className = isSpam ? 'text-spam' : 'text-safe';
        confidenceText.textContent = `Confidence: ${confidencePct}%`;

        // Update status pill
        statusPill.textContent = isSpam ? 'THREAT DETECTED' : 'CLEAR';
        statusPill.className = isSpam ? 'chrome__status is-spam' : 'chrome__status is-safe';

        // Swap idle state for the live result
        idleState.classList.add('hidden');
        resultBox.classList.remove('hidden');

        // Animate threat meter
        requestAnimationFrame(() => {
            meterFill.style.width = `${meterPct}%`;
            meterNeedle.style.left = `${meterPct}%`;
        });

    } catch (error) {
        console.error('Error during prediction:', error);
        statusPill.textContent = 'ERROR';
        statusPill.className = 'chrome__status is-spam';
        alert('An error occurred while analyzing the email. Please check the console.');
    } finally {
        // Reset UI state
        submitBtn.querySelector('.btn-label').textContent = 'Run scan';
        submitBtn.disabled = false;
    }
});