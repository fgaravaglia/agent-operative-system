# Setup your own Design System

## Role

Act as an expensive presentation designer and design-system architect. Bring the judgment and attention to detail I would expect from a senior designer at a leading agency.

## Goal

Create a comprehensive, named design system I can reuse with different AI tools.
My main use is [business presentation slides for finance and ops audiences.] The shared visual rules should also work for websites, dashboards, and other graphics later.

## My reference

I like the visual style of [the attached screenshots] as the specific visual reference.
But my preferences are: [for the main color to be purple]
If I attach other design files, read those too.
Then:

* Study the reference before designing. Identify its color roles, typography hierarchy, spacing, alignment, shapes, component patterns, and use of contrast. * * * Explain briefly what gives it its character.
* Distinguish observed details from estimates and your own design decisions. If you cannot access the website, work from the screenshots and state that limitation.
* Translate the visual language into presentation patterns. Navigation hierarchy can inform section labels, panels can inform content cards, and emphasis can inform takeaway headlines. Use judgment about what transfers. Each slide should communicate one main idea and remain readable when presented.
* Give the system its own identity
* Give it a distinctive name unrelated to the reference brand.

Finally:

* Identify and remove proprietary or licensed assets and brand-specific content from the reference or supplied design files, including logos, trademarks, photography, illustrations, branded copy, and fonts that require a license I have not supplied. Replace them using your own judgment with original elements, openly licensed alternatives, or clearly labeled placeholders. Record what you replaced and any attribution or licensing requirements for replacements.
* If I supply an existing design file, keep its other design rules exactly as written, including layout rules, spacing, type scales, component patterns, and design principles. Those mechanics are the reason I am using it.

Change only what is needed for the replacements above, the new system name, and working file references. Preserve the scale and hierarchy when substituting a font. Put necessary slide adaptations in slides.md and identify them explicitly.

## Output format

Create this folder under '00_Resources'

'''
  design-system/
    DESIGN.md
    slides.md
    design.html
'''
Create complete Markdown files with working relative references:

1. DESIGN.md: The source of truth for the shared visual language. Include the system name, design principles, colors with exact hex values and usage roles, accessible text/background pairings, font families and fallbacks, weights, type hierarchy, spacing scale, alignment rules, borders, corner radii, shadows, icon style, and reusable components. Include chart and table conventions for business data. Use concrete values and examples instead of vague instructions such as “make it clean.” Keep presentation-specific measurements in slides.md.

2. Slides.md: The presentation guide, extending DESIGN.md. Specify a 16:9 slide size, exact margins, grid, content area, title placement, type sizes in points, line spacing, gaps, and minimum readable sizes. Define layouts for a title slide, section divider, executive summary, KPI slide, chart, comparison, table, process, screenshot, and closing. For each layout, give its purpose, arrangement, dimensions, and content limits. Include rules for takeaway headlines, slide rhythm, emphasis, chart labels, and screenshots. Set theme fonts for editable PowerPoint and Google Slides output. When content does not fit, shorten or split it before reducing type below the minimum.

3. design.html: a full, standalone HTML page to illustrate the design system based on DESIGN.md and Slides.md.

## Constraints

* Keep shared values in one source of truth. Do not duplicate the full design system in the instruction files.
* Make the files detailed enough that a fresh AI session can create consistent slides without access to this conversation.
* Check and deliver:
  * Check the files for contradictory rules, missing values, broken paths, and references to removed assets.
  * Deliver the folder as a downloadable ZIP. If file creation is unavailable, provide the complete contents of each file under its exact relative path.

Finish with one short instruction I can paste into a fresh session to create a three-slide test presentation using the folder. Explain how I can later add website.md while keeping DESIGN.md as the shared source of truth.
