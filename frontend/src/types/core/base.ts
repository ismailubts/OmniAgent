export type OmniAgentEventType =
  | "message"
  | "system"
  | "agent_state_changed"
  | "change_agent_state"
  | "run"
  | "read"
  | "write"
  | "edit"
  | "run_ipython"
  | "delegate"
  | "browse"
  | "browse_interactive"
  | "reject"
  | "think"
  | "finish"
  | "error"
  | "recall"
  | "mcp"
  | "call_tool_mcp"
  | "task_tracking"
  | "user_rejected";

export type OmniAgentSourceType = "agent" | "user" | "environment" | "hook";

interface OmniAgentBaseEvent {
  id: number;
  source: OmniAgentSourceType;
  message: string;
  timestamp: string; // ISO 8601
}

export interface OmniAgentActionEvent<
  T extends OmniAgentEventType,
> extends OmniAgentBaseEvent {
  action: T;
  args: Record<string, unknown>;
}

export interface OmniAgentObservationEvent<
  T extends OmniAgentEventType,
> extends OmniAgentBaseEvent {
  cause: number;
  observation: T;
  content: string;
  extras: Record<string, unknown>;
}
