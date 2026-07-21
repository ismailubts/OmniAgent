import { omniAgentApi } from "./omniagent-axios";

class InvariantService {
  static async getPolicy() {
    const { data } = await omniAgentApi.get("/api/security/policy");
    return data.policy;
  }

  static async getRiskSeverity() {
    const { data } = await omniAgentApi.get("/api/security/settings");
    return data.RISK_SEVERITY;
  }

  static async getTraces() {
    const { data } = await omniAgentApi.get("/api/security/export-trace");
    return data;
  }

  static async updatePolicy(policy: string) {
    await omniAgentApi.post("/api/security/policy", { policy });
  }

  static async updateRiskSeverity(riskSeverity: number) {
    await omniAgentApi.post("/api/security/settings", {
      RISK_SEVERITY: riskSeverity,
    });
  }
}

export default InvariantService;
