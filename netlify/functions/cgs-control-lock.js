exports.handler = async function(event) {
  const q = event.queryStringParameters || {};
  let body = {};

  try {
    body = event.body ? JSON.parse(event.body) : {};
  } catch (error) {
    return {
      statusCode: 400,
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        authorization: "BLACK_STOP_WORK",
        reason: "Invalid JSON body",
        controlRule: "Route everything through the box."
      })
    };
  }

  const packageCode = body.packageCode || q.package || null;
  const projectId = body.projectId || q.projectId || null;
  const paymentOrAuthority = body.paymentOrAuthority || q.paymentOrAuthority || null;
  const intakeStatus = body.intakeStatus || q.intakeStatus || null;
  const tier = body.tier || q.tier || null;
  const gate = body.gate || q.gate || null;
  const reviewStatus = body.reviewStatus || q.reviewStatus || null;
  const partnerAuthority = body.partnerAuthority || q.partnerAuthority || "not_required";
  const publicExposure = body.publicExposure || q.publicExposure || "none";

  const allowedPackages = [
    "CGS-DS-029",
    "CGS-GSS-149",
    "CGS-GPF-5000",
    "CGS-CAP-500",
    "CGS-SBIR-3500",
    "CGS-PILOT-7500",
    "CGS-PROVIDER-OPS",
    "CGS-EV-SITE",
    "CGS-FED-COP"
  ];

  const stops = [];
  if (!projectId) stops.push("missing_project_id");
  if (!paymentOrAuthority) stops.push("missing_payment_or_authority");
  if (intakeStatus !== "complete") stops.push("missing_or_incomplete_intake");
  if (!packageCode || !allowedPackages.includes(packageCode)) stops.push("unknown_package_code");
  if (!tier) stops.push("missing_tier");
  if (!gate) stops.push("missing_gate");
  if (tier === "Tier 3" && reviewStatus !== "approved") stops.push("tier_3_without_review");
  if (partnerAuthority === "missing") stops.push("partner_without_authority");
  if (publicExposure === "proprietary_logic") stops.push("public_exposure_of_proprietary_logic");

  if (stops.length > 0) {
    return {
      statusCode: 409,
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        authorization: "BLACK_STOP_WORK",
        stops,
        command: [
          "Protect the engine",
          "Display the capabilities",
          "Sell the packages",
          "Route everything through the box",
          "No uncontrolled custom work",
          "No public exposure of proprietary logic",
          "No delivery without review",
          "No partner representation without authority"
        ]
      })
    };
  }

  return {
    statusCode: 200,
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      authorization: "AUTHORIZED_TO_DRAFT",
      projectId,
      packageCode,
      nextGate: "CGS Review",
      controlRule: "Engine drafts. CGS reviews. Delivery follows archive and dashboard update."
    })
  };
};
