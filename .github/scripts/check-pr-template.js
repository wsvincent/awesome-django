// Checks that a pull request body has the answers the template asks for.
// Returns a list of missing items. An empty list means the template is complete.
// Kept separate from the workflow so it can be run locally:
//   node .github/scripts/check-pr-template.js < body.md

function section(body, startPattern, endPattern) {
  const start = body.search(startPattern);
  if (start === -1) return null;
  const rest = body.slice(start).replace(startPattern, "");
  const end = rest.search(endPattern);
  return end === -1 ? rest : rest.slice(0, end);
}

function hasAnswer(text) {
  if (text === null) return false;
  const cleaned = text
    .replace(/_\(.*?\)_/gs, "") // italic placeholder from the template
    .replace(/^\s*-\s*\[[ x]\].*$/gim, "") // checkbox lines are not prose answers
    .replace(/[-*_\s]/g, "");
  return cleaned.length > 0;
}

function hasCheckedBox(text) {
  return text !== null && /^\s*-\s*\[x\]/im.test(text);
}

function checkTemplate(body) {
  const text = (body || "").replace(/\r\n/g, "\n");
  const missing = [];

  const questions = [
    { n: 1, label: "How long has the project been maintained?" },
    { n: 2, label: "How many releases has it had?" },
    { n: 4, label: "What makes it awesome?" },
  ];

  const info = section(text, /## Project Information/i, /^----|^## /m);
  if (!hasAnswer(section(info || "", /\*\*Project Name:\*\*/i, /^\s*2\./m))) {
    missing.push("Project Information: Project Name");
  }
  if (!hasAnswer(section(info || "", /\*\*Project URL:\*\*/i, /^\s*3\./m))) {
    missing.push("Project Information: Project URL");
  }
  if (!hasAnswer(section(info || "", /\*\*Description:\*\*/i, /^----|^## /m))) {
    missing.push("Project Information: Description");
  }

  const criteria = section(text, /## Criteria/i, /^## /m) || "";
  for (const q of questions) {
    const next = new RegExp(`^\\s*${q.n + 1}\\.\\s+\\*\\*|^----|^## `, "m");
    const answer = section(criteria, new RegExp(`^\\s*${q.n}\\.\\s+\\*\\*.*?\\*\\*`, "m"), next);
    if (!hasAnswer(answer)) missing.push(`Criteria ${q.n}: ${q.label}`);
  }
  const authorship = section(criteria, /^\s*3\.\s+\*\*.*?\*\*/m, /^\s*4\.\s+\*\*|^----|^## /m);
  if (!hasCheckedBox(authorship)) missing.push("Criteria 3: Are you the author? (check one box)");

  const disclosure = section(text, /## AI Disclosure/i, /^----|^## /m);
  if (!hasCheckedBox(disclosure)) missing.push("AI Disclosure (check one box)");

  const company = /^\s*-\s*\[x\].*on behalf of a company/im.test(authorship || "");

  // Question 5 is optional: it asks paid products for a public pricing page.
  const pricing = section(criteria, /^\s*5\.\s+\*\*.*?\*\*/m, /^\s*6\.\s+\*\*|^----|^## /m);
  const hasPricing = /https?:\/\//i.test((pricing || "").replace(/_\(.*?\)_/gs, ""));

  return { missing, company, hasPricing };
}

module.exports = { checkTemplate };

if (require.main === module) {
  const body = require("fs").readFileSync(0, "utf8");
  const result = checkTemplate(body);
  console.log(JSON.stringify(result, null, 2));
  process.exitCode = result.missing.length ? 1 : 0;
}
