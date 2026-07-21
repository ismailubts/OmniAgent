import { OmniAgentParsedEvent } from ".";
import {
  UserMessageAction,
  AssistantMessageAction,
  OmniAgentAction,
  SystemMessageAction,
  CommandAction,
  FinishAction,
  TaskTrackingAction,
} from "./actions";
import {
  AgentStateChangeObservation,
  CommandObservation,
  ErrorObservation,
  MCPObservation,
  OmniAgentObservation,
  TaskTrackingObservation,
} from "./observations";
import { StatusUpdate } from "./variances";

export const isOmniAgentEvent = (
  event: unknown,
): event is OmniAgentParsedEvent =>
  typeof event === "object" &&
  event !== null &&
  "id" in event &&
  "source" in event &&
  "message" in event &&
  "timestamp" in event;

export const isOmniAgentAction = (
  event: OmniAgentParsedEvent,
): event is OmniAgentAction => "action" in event;

export const isOmniAgentObservation = (
  event: OmniAgentParsedEvent,
): event is OmniAgentObservation => "observation" in event;

export const isUserMessage = (
  event: OmniAgentParsedEvent,
): event is UserMessageAction =>
  isOmniAgentAction(event) &&
  event.source === "user" &&
  event.action === "message";

export const isAssistantMessage = (
  event: OmniAgentParsedEvent,
): event is AssistantMessageAction =>
  isOmniAgentAction(event) &&
  event.source === "agent" &&
  (event.action === "message" || event.action === "finish");

export const isErrorObservation = (
  event: OmniAgentParsedEvent,
): event is ErrorObservation =>
  isOmniAgentObservation(event) && event.observation === "error";

export const isCommandAction = (
  event: OmniAgentParsedEvent,
): event is CommandAction => isOmniAgentAction(event) && event.action === "run";

export const isAgentStateChangeObservation = (
  event: OmniAgentParsedEvent,
): event is AgentStateChangeObservation =>
  isOmniAgentObservation(event) && event.observation === "agent_state_changed";

export const isCommandObservation = (
  event: OmniAgentParsedEvent,
): event is CommandObservation =>
  isOmniAgentObservation(event) && event.observation === "run";

export const isFinishAction = (
  event: OmniAgentParsedEvent,
): event is FinishAction =>
  isOmniAgentAction(event) && event.action === "finish";

export const isSystemMessage = (
  event: OmniAgentParsedEvent,
): event is SystemMessageAction =>
  isOmniAgentAction(event) && event.action === "system";

export const isRejectObservation = (
  event: OmniAgentParsedEvent,
): event is OmniAgentObservation =>
  isOmniAgentObservation(event) && event.observation === "user_rejected";

export const isMcpObservation = (
  event: OmniAgentParsedEvent,
): event is MCPObservation =>
  isOmniAgentObservation(event) && event.observation === "mcp";

export const isTaskTrackingAction = (
  event: OmniAgentParsedEvent,
): event is TaskTrackingAction =>
  isOmniAgentAction(event) && event.action === "task_tracking";

export const isTaskTrackingObservation = (
  event: OmniAgentParsedEvent,
): event is TaskTrackingObservation =>
  isOmniAgentObservation(event) && event.observation === "task_tracking";

export const isStatusUpdate = (event: unknown): event is StatusUpdate =>
  typeof event === "object" &&
  event !== null &&
  "status_update" in event &&
  "type" in event &&
  "id" in event;

export const isActionOrObservation = (
  event: OmniAgentParsedEvent,
): event is OmniAgentAction | OmniAgentObservation =>
  isOmniAgentAction(event) || isOmniAgentObservation(event);
