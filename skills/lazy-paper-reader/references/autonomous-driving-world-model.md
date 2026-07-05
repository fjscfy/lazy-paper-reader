# Autonomous-Driving World-Model Review Profile

Load this profile only for autonomous-driving world models, world-action models, neural simulators, generative driving models, or closely related sensor-simulation papers.

## World representation and prediction target

- Identify the world representation: pixels, continuous latent, discrete tokens, BEV, occupancy, agents, 3D/4D scene, or a hybrid.
- State exactly what is predicted: next observation, future video, future state, agent motion, reward, value, action, or reconstruction parameters.
- Ask what driving-relevant information the encoder may discard.

## Conditions and provenance

- Define every action mathematically: control, ego state, trajectory, navigation command, or intent.
- Trace each structured condition to vehicle logs, offline labels, HD maps, future annotations, or an upstream perception model.
- Check whether future 3D boxes, trajectories, maps, or layouts reveal part of the answer.
- Distinguish controllable rendering from learned environment dynamics.

## Components and training

- Separate encoder/tokenizer, dynamics or world model, decoder/renderer, condition encoder, reward model, planner, and policy.
- Mark each component as trained, pretrained, frozen, or fixed.
- Compare teacher-forced training inputs with free-rollout inference inputs.
- Identify the actual optimization target and whether it rewards visual realism or decision-useful prediction.

## Temporal, multiview, and geometric consistency

- Check temporal identity, motion, occlusion, and long-horizon drift.
- Check multiview overlap and shared-object consistency.
- Determine whether consistency comes from attention, camera geometry, 3D representation, adjacent-view conditioning, or post-processing.

## System role and decision interface

- Classify the method as generator, data engine, renderer, simulator, predictor, candidate evaluator, reranker, planner, or policy.
- If candidates are supplied externally, state that performance is bounded by the candidate set.
- Trace how generated pixels or latent features enter reward and final action selection.
- Check whether the reward uses open visual information or compresses the future back into boxes, lanes, and hand-written distances.

## Counterfactual and closed-loop validity

- Distinguish camera-trajectory rerendering from a causal intervention on ego action.
- Ask whether other agents react or merely replay logged trajectories.
- Check whether a counterfactual has geometric, simulated, paired, or real ground truth.
- Separate open-loop prediction from closed-loop interaction.
- Do not treat FID, FVD, visual quality, or action-conditioned generation as evidence of causal dynamics or safety.

## Uncertainty and deployment

- Separate multimodal future uncertainty from model error when possible.
- Check calibration, failure detection, conservative fallback, and reward uncertainty.
- Record rollout horizon, sampling steps, camera count, resolution, candidate count, hardware, latency, memory, and planning frequency.

## Evidence strength

Stronger evidence includes controlled interventions, reactive agents, long-horizon consistency, calibrated uncertainty, downstream decision gains, closed-loop evaluation, multiple datasets, fair baselines, and complete resource reporting.

Weaker evidence includes selected videos, perceptual metrics alone, future structured conditions, fixed non-reactive agents, open-loop-only results, unreported latency, and claims that generation implies world understanding.
